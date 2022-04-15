#nullable disable
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using AppWeb.Data;
using AppWeb.Models;

namespace AppWeb.Controllers
{
  public class SuppliersController : Controller
  {
    private readonly Context _context;
    private readonly ILogger<SuppliersController> _logger;

    public SuppliersController(Context context, ILogger<SuppliersController> logger)
    {
      _context = context;
      _logger = logger;
    }

    // GET: Suppliers
    public async Task<IActionResult> Index()
    {
      _logger.LogInformation(($"O usuário {User.Identity.Name} listou fornecedores.").ToString());
      return View(await _context.Suppliers.ToListAsync());
    }

    // GET: Suppliers/Details/5
    public async Task<IActionResult> Details(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var supplier = await _context.Suppliers
          .FirstOrDefaultAsync(m => m.Id == id);
      if (supplier == null)
      {
        return NotFound();
      }

      _logger.LogInformation(($"O usuário {User.Identity.Name} buscou o fornecedor {supplier.FantasyName}.").ToString());
      return View(supplier);
    }

    // GET: Suppliers/Create
    public IActionResult Create()
    {
      return View();
    }

    // POST: Suppliers/Create
    // To protect from overposting attacks, enable the specific properties you want to bind to.
    // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("Id,FantasyName,LegalName,CNPJ")] Supplier supplier)
    {
      if (ModelState.IsValid)
      {
        _context.Add(supplier);
        await _context.SaveChangesAsync();

        _logger.LogInformation(($"O usuário {User.Identity.Name} criou o fornecedor {supplier.FantasyName}.").ToString());

        return RedirectToAction(nameof(Index));
      }
      return View(supplier);
    }

    // GET: Suppliers/Edit/5
    public async Task<IActionResult> Edit(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var supplier = await _context.Suppliers.FindAsync(id);
      if (supplier == null)
      {
        return NotFound();
      }
      return View(supplier);
    }

    // POST: Suppliers/Edit/5
    // To protect from overposting attacks, enable the specific properties you want to bind to.
    // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Edit(int id, [Bind("Id,FantasyName,LegalName,CNPJ")] Supplier supplier)
    {
      if (id != supplier.Id)
      {
        return NotFound();
      }

      if (ModelState.IsValid)
      {
        try
        {
          _context.Update(supplier);
          await _context.SaveChangesAsync();

          _logger.LogInformation(($"O usuário {User.Identity.Name} editou o fornecedor {supplier.FantasyName}.").ToString());
        }
        catch (DbUpdateConcurrencyException)
        {
          if (!SupplierExists(supplier.Id))
          {
            return NotFound();
          }
          else
          {
            throw;
          }
        }
        return RedirectToAction(nameof(Index));
      }
      return View(supplier);
    }

    // GET: Suppliers/Delete/5
    public async Task<IActionResult> Delete(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var supplier = await _context.Suppliers
          .FirstOrDefaultAsync(m => m.Id == id);
      if (supplier == null)
      {
        return NotFound();
      }

      return View(supplier);
    }

    // POST: Suppliers/Delete/5
    [HttpPost, ActionName("Delete")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> DeleteConfirmed(int id)
    {
      var supplier = await _context.Suppliers.FindAsync(id);
      _context.Suppliers.Remove(supplier);
      await _context.SaveChangesAsync();

      _logger.LogInformation(($"O usuário {User.Identity.Name} excluiu o fornecedor {supplier.FantasyName}.").ToString());

      return RedirectToAction(nameof(Index));
    }

    private bool SupplierExists(int id)
    {
      return _context.Suppliers.Any(e => e.Id == id);
    }
  }
}
