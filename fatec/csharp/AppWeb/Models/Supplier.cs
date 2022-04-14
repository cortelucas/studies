using System.ComponentModel.DataAnnotations;

namespace AppWeb.Models
{
    public class Supplier
    {
        [Key]
        public int Id { get; set; }
        public string? FantasyName { get; set; }
        public string? LegalName { get; set; }
        public string? CNPJ { get; set; }
    }
}