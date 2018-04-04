from django.contrib import admin

from cryptocoins.models import Cryptocurrency, FavouriteCoin


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price_usd', 'rank', 'volume_usd_24h',
                    'total_supply', 'last_updated')


@admin.register(FavouriteCoin)
class FavouriteCoinAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin')
