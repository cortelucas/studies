using AppWeb.Models;
using Microsoft.EntityFrameworkCore;

namespace AppWeb.Data
{
  public class Context : DbContext
  {
    public Context(DbContextOptions<Context> options) : base(options) { }
    public DbSet<Client> Clients { get; set; }
    public DbSet<Product> Products { get; set; }
    public DbSet<Inventory> Inventories { get; set; }
    public DbSet<Supplier> Suppliers { get; set; }
  }
}