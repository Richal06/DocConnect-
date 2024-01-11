from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("pres/",views.pres,name='prescription'),

    path('payment/', views.homepage, name='index'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('admin/', admin.site.urls),
    path('paytm/', views.paytm, name="paytm"),
    path('Orderss/<int:id>', views.members, name='details'),
    path('pay/',views.ff,name="pay")
    ]

