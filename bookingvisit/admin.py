from django.contrib import admin
from .models import Hairdresser, HServices, BServices, Beautician, Reservation_Hairdresser, Reservation_Beautician, Client_Profil, Opinions

admin.site.register(Hairdresser)
admin.site.register(HServices)
admin.site.register(Beautician)
admin.site.register(BServices)
admin.site.register(Reservation_Hairdresser)
admin.site.register(Reservation_Beautician)
admin.site.register(Client_Profil)
admin.site.register(Opinions)
