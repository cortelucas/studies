using System.ComponentModel.DataAnnotations;

namespace AppWeb.Models
{
    public class Inventory
    {
        [Key]
        public int Id { get; set; }
        public int ProductId { get; set; }
        public virtual Product? Product { get; set; }
        public int SupplierId { get; set; }
        public virtual Supplier? Supplier { get; set; }
        public int Quantity { get; set; }
    }
}