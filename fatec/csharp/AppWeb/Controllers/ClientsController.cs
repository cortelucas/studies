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
using Microsoft.AspNetCore.Authorization;

namespace AppWeb.Controllers
{
  [Authorize]
  public class ClientsController : Controller
  {
    private readonly Context _context;
    private readonly ILogger<ClientsController> _logger;

    public ClientsController(Context context, ILogger<ClientsController> logger)
    {
      _context = context;
      _logger = logger;
    }

    // GET: Clients
    public async Task<IActionResult> Index()
    {
      _logger.LogInformation(($"O usuário {User.Identity.Name} listou os clientes!").ToString());
      return View(await _context.Clients.ToListAsync());
    }

    // GET: Clients/Details/5
    public async Task<IActionResult> Details(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var client = await _context.Clients
          .FirstOrDefaultAsync(m => m.Id == id);
      if (client == null)
      {
        return NotFound();
      }

      _logger.LogInformation(($"O usuário {User.Identity.Name} pesquisou pelo cliente {client.Name} .").ToString());

      return View(client);
    }

    // GET: Clients/Create
    public IActionResult Create()
    {
      return View();
    }

    // POST: Clients/Create
    // To protect from overposting attacks, enable the specific properties you want to bind to.
    // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("Id,Name,Email,CPF")] Client client)
    {
      if (ModelState.IsValid)
      {
        _context.Add(client);
        await _context.SaveChangesAsync();

        _logger.LogInformation(($"O usuário {User.Identity.Name} criou o cliente {client.Name} .").ToString());

        return RedirectToAction(nameof(Index));
      }
      return View(client);
    }

    // GET: Clients/Edit/5
    public async Task<IActionResult> Edit(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var client = await _context.Clients.FindAsync(id);
      if (client == null)
      {
        return NotFound();
      }

      return View(client);
    }

    // POST: Clients/Edit/5
    // To protect from overposting attacks, enable the specific properties you want to bind to.
    // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Email,CPF")] Client client)
    {
      if (id != client.Id)
      {
        return NotFound();
      }

      if (ModelState.IsValid)
      {
        try
        {
          _context.Update(client);
          await _context.SaveChangesAsync();

          _logger.LogInformation(($"O usuário {User.Identity.Name} edito o cliente {client.Name} .").ToString());
        }
        catch (DbUpdateConcurrencyException)
        {
          if (!ClientExists(client.Id))
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
      return View(client);
    }

    // GET: Clients/Delete/5
    public async Task<IActionResult> Delete(int? id)
    {
      if (id == null)
      {
        return NotFound();
      }

      var client = await _context.Clients
          .FirstOrDefaultAsync(m => m.Id == id);
      if (client == null)
      {
        return NotFound();
      }

      return View(client);
    }

    // POST: Clients/Delete/5
    [HttpPost, ActionName("Delete")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> DeleteConfirmed(int id)
    {
      var client = await _context.Clients.FindAsync(id);
      _context.Clients.Remove(client);
      await _context.SaveChangesAsync();
      _logger.LogInformation(($"O usuário {User.Identity.Name} excluiu o cliente {client.Name} .").ToString());
      return RedirectToAction(nameof(Index));
    }

    private bool ClientExists(int id)
    {
      return _context.Clients.Any(e => e.Id == id);
    }
  }
}
