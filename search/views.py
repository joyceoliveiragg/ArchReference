from django.shortcuts import render

# Create your views here.
#terminar de definir o context para os outro filtros
#TODO -> criar funções de JS para click e consumir crawler
def index(request):
    context = {
        'categorias': ['Residential Architecture', 'Houses', 'Refurbishment', 'Commercial & Offices', 'Cultural Architecture', 'Interior Design', 'Educational Architecture', 'Housing', 'Hospitality Architecture', 'Renovation', 'Apartments', 'Museums & Exhibit', 'Residential Interiors'  ],
        'climas': ['subtropical', 'tropical', 'semiarid', 'mediterrain', 'humid subtropical', 'subartic', 'arid', 'marine west coast', 'temperate oceanic', 'temperate continental', 'tundra', 'equatoriial', 'mountainous terrain', 'polar'  ],
        'movimentos': ['Bauhaus','Vkhutemas', 'eaux-Art', 'Glasgow School of Air', 'Brutalism','Postmodern Industrialism', 'Art Nouveau', 'Postmodern', 'Contemporary Architecture', 'Classical', 'Romanesque', 'Gothic', 'Baroque', 'Neoclassical', 'Art Deco', 'Modern', 'Deconstructivism' ],
        'materiais': ['brick', 'concrete', 'fabric', 'glass', 'other', 'plastic', 'steel', 'stone', 'wood' ],
        'cores': ['red','violet','blue','green', 'yellow','orange'],
        'areas': ['8m²-15m²', '15m²-25m²', '25m²-45m²', '45m²-75m²', '75m²-100m²', '100m²-120m²', '120m²-150m²', '150m²-180m²', '180m²-200m²', '200m²+' ],
    }
    return render(request, "landingPage/index.html", context)