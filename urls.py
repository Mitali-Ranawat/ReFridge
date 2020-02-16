from django.conf.urls import url
from . import views

urlpatterns = [

	url('^$',views.index,name= 'index'),
    url('^index$',views.index,name= 'Index'),
    url('^Login/$',views.Login,name = 'Login'),

    url('^loginVerify/$',views.verifyLogin),
    url('^logout/$',views.logout),

    url('^Signup/$',views.Signup),
    url('^addSEL/$',views.addsel),
    url('^ordAPP/$',views.ordAPP),
    url('^ordORG/$',views.ordORG),
    url('^ordBAN/$',views.ordBAN),
    url('^ordPEA/$',views.ordPEA),
    url('^ordPIN/$',views.ordPIN),
    url('^ordCHE/$',views.ordCHE),
    url('^selectsel/$',views.selectsel),
    url('^selectbuy/$',views.selectbuy),


    url('^signup/$',views.signup),
    url('^adminDashboard/$',views.adminDash),
    url('^buyerDashboard/$',views.buyerDash),
    url('^sellerDashboard/$',views.sellerDash),
    url('^openfridge/$',views.openFridge),
    url('^openorder/$',views.openOrder),
    url('^openstock/$',views.openStock),


    url('^sendmail/$',views.email),

    url('^addbuyer/$',views.addbuyer),
    url('^addseller/$',views.addseller),
    url('^addproduct/$',views.addproduct),
    url('^weeklyreport/$',views.weeklyreport),
    url('^buyerwisereport/$',views.buyerwisereport),
    url('^sellerwisereport/$',views.sellerwisereport),

    url('^buyerprofile/$',views.buyerprofile),
    url('^buyercashdetails/$',views.buyercashdetails),
    url('^buyerfridgestatus/$',views.buyerfridgestatus),
    url('^buyerreport/$',views.buyerreport),

    url('^sellerprofile/$',views.sellerprofile),
    url('^sellercashdetails/$',views.sellercashdetails),
    url('^sellerreport/$',views.sellerreport),

    url('^fridgestocks/$',views.fridgestocks),
    url('^fridgeaddproducts/$',views.fridgeaddproducts),
    url('^fridgeeditproducts/$',views.fridgeeditproducts),

    url('^placeorder/$',views.placeorder),
    url('^ordercashdetails/$',views.ordercashdetails),
    url('^buyerorderhistory/$',views.buyerorderhistory),
    url('^suggestions/$',views.suggestions),

    url('^sellerstock/$',views.sellerstock),
    url('^sellerorderhistory/$',views.sellerorderhistory),
    url('^sellercashdetail/$',views.sellercashdetail),

    url('^addP/$',views.addP),
    url('^addB/$',views.addB),
    url('^addcashS/$',views.addcashS),
    url('^addcashB/$',views.addcashB),
    url('^addfpro/$',views.addfpro),
    url('^addSTO/$',views.addSTO),
    url('^fridgeProducts/$',views.fridgeProducts),
]