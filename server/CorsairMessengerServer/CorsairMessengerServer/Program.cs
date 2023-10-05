
using CorsairMessengerServer.Data;
using CorsairMessengerServer.Data.Repositories.Users;
using CorsairMessengerServer.Data.Repositories.WebTokens;
using CorsairMessengerServer.Managers;
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
                    options.TokenValidationParameters = new TokenValidationParameters()
                    {
                        ValidIssuer = AuthOptions.ISSUER,
                        ValidateIssuer = true,
                        ValidAudience = AuthOptions.AUDIENCE,
                        ValidateAudience = true,
                        ValidateLifetime = true,
                        IssuerSigningKey = AuthOptions.SymmetricSecurityKey,
                        ValidateIssuerSigningKey = true,
                    };
                });

            var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

            builder.Services.AddDbContext<DataContext>(options =>
            {
                options.UseNpgsql(connectionString);
            });

            builder.Services.AddTransient<IPasswordHasher, Sha256PasswordHasher>();
            builder.Services.AddTransient<IMessageBroker, QueryMessageBroker>();

            builder.Services.AddTransient<WebTokensManager>();
            
            builder.Services.AddScoped<IUserRepository, UserRepository>();
            builder.Services.AddScoped<IWebTokensRepository, WebTokensRepository>();

            var app = builder.Build();

            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.UseHttpsRedirection();
            app.UseAuthorization();
            app.MapControllers();
            app.UseWebSockets();


            app.Run();
        }
    }
}