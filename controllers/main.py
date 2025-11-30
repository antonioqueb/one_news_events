from odoo import http
from odoo.http import request, Response
import json

class OneNewsEventsController(http.Controller):

    @http.route(['/api/news-events'], type='http', auth='public', methods=['GET'], cors='*')
    def get_events_list(self, **kwargs):
        events = request.env['one.event'].sudo().search([])
        
        data_list = []
        for ev in events:
            # Usamos el helper del modelo para obtener la URL correcta
            img_url = ev.get_main_image_url()
            
            data_list.append({
                "id": ev.id,
                "slug": ev.slug,
                "status": ev.status,
                "date": ev.date_display or "",
                "title": ev.name,
                "location": ev.location or "",
                "description": ev.description_short or "",
                "image": img_url
            })

        response = {"data": data_list}
        return Response(json.dumps(response), headers={'Content-Type': 'application/json'})

    @http.route('/api/news-events/<string:slug>', type='http', auth='public', methods=['GET'], cors='*')
    def get_event_detail(self, slug, **kwargs):
        event = request.env['one.event'].sudo().search([('slug', '=', slug)], limit=1)

        if not event:
            return Response(json.dumps({"error": "Not Found"}), status=404, headers={'Content-Type': 'application/json'})

        # Construir galería usando la lógica híbrida
        gallery_urls = [g.get_gallery_image_url() for g in event.gallery_ids]

        event_data = {
            "id": event.id,
            "slug": event.slug,
            "status": event.status,
            "date": event.date_display or "",
            "time": event.time_display or "",
            "title": event.name,
            "location": event.location or "",
            "organizer": event.organizer or "",
            "contact": event.contact or "",
            "description": event.description_short or "",
            "long_description": event.description_long or "",
            "image": event.get_main_image_url(),
            "gallery": gallery_urls
        }

        response = {"data": event_data}
        return Response(json.dumps(response), headers={'Content-Type': 'application/json'})
