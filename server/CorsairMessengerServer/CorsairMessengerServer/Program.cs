using CorsairMessengerServer.Data;
using CorsairMessengerServer.Data.Repositories;
using CorsairMessengerServer.Managers;
using CorsairMessengerServer.Middlewares.Extensions;
using CorsairMessengerServer.Services.MessageBrokers;
using CorsairMessengerServer.Services.PasswordHasher;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;

namespace CorsairMessengerServer
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            builder.Services.AddControllers();
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();
            builder.Services.AddAuthorization();

            builder.Services
                .AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
                .AddJwtBearer(options =>
                {
                    options.TokenValidationParameters = new TokenValidationParameters
                    {
                        ValidateIssuer = false,
                        ValidateAudience = false,
                        ValidateLifetime = false,
                        ValidateIssuerSigningKey = true,
                        IssuerSigningKey = AuthOptions.SymmetricSecurityKey,
                    };
                });

            var dbConnectionString = builder.Configuration.GetConnectionString("DatabaseConnection");

            builder.Services.AddDbContext<DataContext>(options =>
            {
                options.UseNpgsql(dbConnectionString);
            });

            var redisSection = builder.Configuration.GetSection("Redis");

            builder.Services.AddStackExchangeRedisCache(options =>
            {
                options.Configuration = redisSection.GetValue<string>("Configuration");
                options.InstanceName = redisSection.GetValue<string>("InstanceName");
            });

            builder.Services.AddTransient<WebSocketsManager>();

            builder.Services.AddTransient<UsersRepository>();
            builder.Services.AddTransient<MessagesRepository>();
            builder.Services.AddTransient<WebSocketsRepository>();

            builder.Services.AddTransient<IPasswordHasher, Sha256PasswordHasher>();
            builder.Services.AddTransient<IMessageBroker, AsyncMessageBroker>();

            var app = builder.Build();

            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.MapControllers();

            app.UseHttpsRedirection();
            app.UseAuthentication();
            app.UseAuthorization();
            app.UseSessionValidityCheck();
            app.UseWebSockets();
            app.UseWebSocketsConnections();

            app.Run();
        }
    }
}