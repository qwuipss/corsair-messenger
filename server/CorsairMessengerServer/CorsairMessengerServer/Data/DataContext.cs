using CorsairMessengerServer.Data.Entities;
using Microsoft.EntityFrameworkCore;

namespace CorsairMessengerServer.Data
{
    public class DataContext : DbContext
    {
        public DbSet<User> Users { get; set; } = null!;

        public DataContext(DbContextOptions<DataContext> options) : base(options)
        {
            Database.EnsureDeleted();
            Database.EnsureCreated();
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<User>().Property(user => user.Nickname).HasColumnType("VARCHAR(25)");

            modelBuilder.Entity<User>().ToTable(table => table.HasCheckConstraint("Nickname", "LENGTH(\"Nickname\") BETWEEN 5 AND 25"));

            modelBuilder.Entity<User>().HasAlternateKey(user => user.Nickname);
            modelBuilder.Entity<User>().HasAlternateKey(user => user.Email);
        }
    }
}
