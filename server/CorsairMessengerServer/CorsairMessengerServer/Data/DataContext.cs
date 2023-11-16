using CorsairMessengerServer.Data.Entities;
using Microsoft.EntityFrameworkCore;
using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;

namespace CorsairMessengerServer.Data
{
    public class DataContext : DbContext
    {
        public DbSet<UserEntity> Users { get; set; } = null!;

        public DbSet<MessageEntity> Messages { get; set; } = null!;

        public DataContext(DbContextOptions<DataContext> options) : base(options)
        {
            Database.EnsureCreated();
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<UserEntity>().ToTable(table =>
                table.HasCheckConstraint("Nickname", $"LENGTH(\"Nickname\") >= {NICKNAME_MIN_LENGTH}"));

            modelBuilder.Entity<UserEntity>().HasAlternateKey(user => user.Nickname);
            modelBuilder.Entity<UserEntity>().HasAlternateKey(user => user.Email);
        }
    }
}
