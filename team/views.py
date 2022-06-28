from django.shortcuts import render
from .models import opggData
# Create your views here.
def t1(request):
  return render(request, 'team/t1/t1.html')


#t1

def t1_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/t1/t1_T.html',
        {"datas":data}
    )
def t1_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/t1/t1_J.html',
        {"datas":data}
    )
def t1_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/t1/t1_M.html',
        {"datas":data}
    )
def t1_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/t1/t1_A.html',
        {"datas":data}
    )
def t1_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/t1/t1_S.html',
        {"datas":data}
    )

# dk

def dk(request):
  return render(request, 'team/dk/dk.html')

def dk_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/dk/dk_T.html',
        {"datas":data}
    )
def dk_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/dk/dk_J.html',
        {"datas":data}
    )
def dk_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/dk/dk_M.html',
        {"datas":data}
    )
def dk_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/dk/dk_A.html',
        {"datas":data}
    )
def dk_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/dk/dk_S.html',
        {"datas":data}
    )

# gen

def gen(request):
  return render(request, 'team/gen/gen.html')

def gen_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/gen/gen_T.html',
        {"datas":data}
    )
def gen_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/gen/gen_J.html',
        {"datas":data}
    )
def gen_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/gen/gen_M.html',
        {"datas":data}
    )
def gen_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/gen/gen_A.html',
        {"datas":data}
    )
def gen_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/gen/gen_S.html',
        {"datas":data}
    )

# drx

def drx(request):
  return render(request, 'team/drx/drx.html')

def drx_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/drx/drx_T.html',
        {"datas":data}
    )
def drx_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/drx/drx_J.html',
        {"datas":data}
    )
def drx_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/drx/drx_M.html',
        {"datas":data}
    )
def drx_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/drx/drx_A.html',
        {"datas":data}
    )
def drx_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/drx/drx_S.html',
        {"datas":data}
    )

# lsb

def lsb(request):
  return render(request, 'team/lsb/lsb.html')

def lsb_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/lsb/lsb_T.html',
        {"datas":data}
    )
def lsb_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/lsb/lsb_J.html',
        {"datas":data}
    )
def lsb_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/lsb/lsb_M.html',
        {"datas":data}
    )
def lsb_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/lsb/lsb_A.html',
        {"datas":data}
    )
def lsb_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/lsb/lsb_S.html',
        {"datas":data}
    )

# kt

def kt(request):
  return render(request, 'team/kt/kt.html')

def kt_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kt/kt_T.html',
        {"datas":data}
    )
def kt_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kt/kt_J.html',
        {"datas":data}
    )
def kt_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kt/kt_M.html',
        {"datas":data}
    )
def kt_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kt/kt_A.html',
        {"datas":data}
    )
def kt_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kt/kt_S.html',
        {"datas":data}
    )

# kdf

def kdf(request):
  return render(request, 'team/kdf/kdf.html')

def kdf_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kdf/kdf_T.html',
        {"datas":data}
    )
def kdf_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kdf/kdf_J.html',
        {"datas":data}
    )
def kdf_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kdf/kdf_M.html',
        {"datas":data}
    )
def kdf_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kdf/kdf_A.html',
        {"datas":data}
    )
def kdf_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/kdf/kdf_S.html',
        {"datas":data}
    )

# hle

def hle(request):
  return render(request, 'team/hle/hle.html')

def hle_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/hle/hle_T.html',
        {"datas":data}
    )
def hle_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/hle/hle_J.html',
        {"datas":data}
    )
def hle_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/hle/hle_M.html',
        {"datas":data}
    )
def hle_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/hle/hle_A.html',
        {"datas":data}
    )
def hle_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/hle/hle_S.html',
        {"datas":data}
    )

# bro

def bro(request):
  return render(request, 'team/bro/bro.html')

def bro_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/bro/bro_T.html',
        {"datas":data}
    )
def bro_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/bro/bro_J.html',
        {"datas":data}
    )
def bro_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/bro/bro_M.html',
        {"datas":data}
    )
def bro_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/bro/bro_A.html',
        {"datas":data}
    )
def bro_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/bro/bro_S.html',
        {"datas":data}
    )
    
# ns

def ns(request):
  return render(request, 'team/ns/ns.html')

def ns_T(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/ns/ns_T.html',
        {"datas":data}
    )
def ns_J(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/ns/ns_J.html',
        {"datas":data}
    )
def ns_M(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/ns/ns_M.html',
        {"datas":data}
    )
def ns_A(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/ns/ns_A.html',
        {"datas":data}
    )
def ns_S(request):
    data = opggData.objects.all()
    return render(
        request,
        'team/ns/ns_S.html',
        {"datas":data}
    )






