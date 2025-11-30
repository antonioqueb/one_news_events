{
    'name': 'One News & Events Manager',
    'version': '1.1',
    'summary': 'Full Backend for Next.js Events API with Image Uploads',
    'description': """
        Backend system to manage Events and News.
        Features:
        - Image Upload (Binary) + External URL support.
        - Gallery Management.
        - API REST endpoints: /api/news-events
    """,
    'category': 'Website',
    'author': 'Tu Nombre',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': '/base/static/description/icon.png',
}
