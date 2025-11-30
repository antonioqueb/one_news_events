from odoo import models, fields, api

class OneEvent(models.Model):
    _name = 'one.event'
    _description = 'News and Events Management'
    _order = 'id desc'
    # IMPORTANTE: Eliminada la línea _inherit = ['website.seo.metadata']

    name = fields.Char(string='Title', required=True)
    slug = fields.Char(string='Slug (URL Friendly)', required=True, copy=False, help="Identificador único para la URL del frontend")
    
    status = fields.Selection([
        ('upcoming', 'Upcoming (Blinking Black)'),
        ('past', 'Past (Gray)')
    ], string='Status', default='upcoming', required=True)

    # Fechas y Textos
    date_display = fields.Char(string='Date Label', help="Ej: Spring 2024")
    time_display = fields.Char(string='Time Label', help="Ej: 10:00 AM - 6:00 PM")
    location = fields.Char(string='Location')
    organizer = fields.Char(string='Organizer')
    contact = fields.Char(string='Contact Info')
    
    description_short = fields.Text(string='Short Description')
    description_long = fields.Html(string='Long Description', sanitize=False)

    # --- GESTIÓN DE IMÁGENES ---
    image_file = fields.Image(string="Upload Main Image", max_width=1920, max_height=1920)
    image_external_url = fields.Char(string="External Image URL", help="Usa esto si no subes imagen local")

    # Galería
    gallery_ids = fields.One2many('one.event.gallery', 'event_id', string='Gallery Images')

    _sql_constraints = [
        ('slug_unique', 'unique(slug)', 'The slug must be unique!')
    ]

    def get_main_image_url(self):
        """ Retorna la URL local si existe imagen, sino la externa """
        self.ensure_one()
        # Esto funciona con 'base', no necesita 'website'
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if self.image_file:
            return f"{base_url}/web/image/one.event/{self.id}/image_file"
        return self.image_external_url or ""

class OneEventGallery(models.Model):
    _name = 'one.event.gallery'
    _description = 'Event Gallery Item'
    # Eliminamos sequence del order si daba problemas, o lo dejamos si ya quitamos el widget handle
    _order = 'id' 

    event_id = fields.Many2one('one.event', string='Event', ondelete='cascade')
    
    image_file = fields.Image(string="Upload Gallery Image", max_width=1920, max_height=1920)
    image_external_url = fields.Char(string="External URL", help="Fallback si no hay imagen subida")

    def get_gallery_image_url(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if self.image_file:
            return f"{base_url}/web/image/one.event.gallery/{self.id}/image_file"
        return self.image_external_url or ""