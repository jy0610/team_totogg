from django.urls import path
from . import views


urlpatterns = [
    #t1
    path('t1/', views.t1),
    path('t1_T/', views.t1_T),
    path('t1_J/', views.t1_J),
    path('t1_M/', views.t1_M),
    path('t1_A/', views.t1_A),
    path('t1_S/', views.t1_S),
    
    #dk
    path('dk/', views.dk),
    path('dk_T/', views.dk_T),
    path('dk_J/', views.dk_J),
    path('dk_M/', views.dk_M),
    path('dk_A/', views.dk_A),
    path('dk_S/', views.dk_S),
    
    #drx
    path('drx/', views.drx),
    path('drx_T/', views.drx_T),
    path('drx_J/', views.drx_J),
    path('drx_M/', views.drx_M),
    path('drx_A/', views.drx_A),
    path('drx_S/', views.drx_S),

    #gen
    path('gen/', views.gen),
    path('gen_T/', views.gen_T),
    path('gen_J/', views.gen_J),
    path('gen_M/', views.gen_M),
    path('gen_A/', views.gen_A),
    path('gen_S/', views.gen_S),

    #lsb
    path('lsb/', views.lsb),
    path('lsb_T/', views.lsb_T),
    path('lsb_J/', views.lsb_J),
    path('lsb_M/', views.lsb_M),
    path('lsb_A/', views.lsb_A),
    path('lsb_S/', views.lsb_S),

    #kdf
    path('kdf/', views.kdf),
    path('kdf_T/', views.kdf_T),
    path('kdf_J/', views.kdf_J),
    path('kdf_M/', views.kdf_M),
    path('kdf_A/', views.kdf_A),
    path('kdf_S/', views.kdf_S),

    #kt
    path('kt/', views.kt),
    path('kt_T/', views.kt_T),
    path('kt_J/', views.kt_J),
    path('kt_M/', views.kt_M),
    path('kt_A/', views.kt_A),
    path('kt_S/', views.kt_S),

    #hle
    path('hle/', views.hle),
    path('hle_T/', views.hle_T),
    path('hle_J/', views.hle_J),
    path('hle_M/', views.hle_M),
    path('hle_A/', views.hle_A),
    path('hle_S/', views.hle_S),

    #ns
    path('ns/', views.ns),
    path('ns_T/', views.ns_T),
    path('ns_J/', views.ns_J),
    path('ns_M/', views.ns_M),
    path('ns_A/', views.ns_A),
    path('ns_S/', views.ns_S),

    #bro
    path('bro/', views.bro),
    path('bro_T/', views.bro_T),
    path('bro_J/', views.bro_J),
    path('bro_M/', views.bro_M),
    path('bro_A/', views.bro_A),
    path('bro_S/', views.bro_S),

]