from django.shortcuts import render

# Create your views here.
#terminar de definir o context para os outro filtros
#TODO -> criar funções de JS para click e consumir crawler
def index(request):
    context = {
        'categorias': ['Residential Architecture', 'Houses', 'Refurbishment', 'Commercial & Offices', 'Cultural Architecture', 'Interior Design', 'Educational Architecture', 'Housing', 'Hospitality Architecture', 'Renovation', 'Apartments', 'Museums & Exhibit', 'Residential Interiors'  ],
        'climas': ['subtropical', 'tropical', 'semiarid', 'mediterrain', 'humid subtropical', 'subartic', 'arid', 'marine west coast', 'temperate oceanic', 'temperate continental', 'tundra', 'equatoriial', 'mountainous terrain', 'polar'  ],
        
        'materiais': ['brick', 'concrete', 'fabric', 'glass', 'other', 'plastic', 'steel', 'stone', 'wood' ],
    }
    return render(request, "landingPage/index.html", context)