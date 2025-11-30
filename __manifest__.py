{
    'name': 'One News & Events Manager',
    'version': '1.2',
    'summary': 'Full Backend for Next.js Events API',
    'description': """
        Backend system to manage Events and News.
        Features:
        - Image Upload (Binary) + External URL support.
        - API REST endpoints: /api/news-events
    """,
    'category': 'Backend',
    'author': 'Alphaqueb Consulting',
    'depends': ['base', 'web'], 
    'data': [
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}