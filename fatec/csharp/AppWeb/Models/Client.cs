using System.ComponentModel.DataAnnotations;

namespace AppWeb.Models
{
    public class Client
    {
     [Key]
        public int Id { get; set; }
        public string? Name { get; set; }
        public string? Email { get; set; }
        public string? CPF { get; set; }   
    }
}