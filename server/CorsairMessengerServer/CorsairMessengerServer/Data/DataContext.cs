using CorsairMessengerServer.Data.Entities;
using Microsoft.EntityFrameworkCore;
using static CorsairMessengerServer.Data.Constraints.UserEntityConstraints;

namespace CorsairMessengerServer.Data
{
    public class DataContext : DbContext
    {
        public DbSet<User> Users { get; set; } = null!;

        public DbSet<Message> Messages { get; set; } = null!;

        public DataContext(DbContextOptions<DataContext> options) : base(options)
        {
            Database.EnsureCreated();
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<User>().ToTable(table =>
                table.HasCheckConstraint("Nickname", $"LENGTH(\"Nickname\") >= {NICKNAME_MIN_LENGTH}"));

            modelBuilder.Entity<User>().HasAlternateKey(user => user.Nickname);
            modelBuilder.Entity<User>().HasAlternateKey(user => user.Email);
        }
    }
}
