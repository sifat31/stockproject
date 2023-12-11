from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models.json_models import JsonModel
from .models.sql_models import SqlModel
from .forms import SqlModelForm  # Create this form in the next step
import pandas as pd



def stock_data_view(request):
    stock_data = JsonModel.objects.all().values()
    return render(request, 'stock_data.html', {'stock_data': stock_data})


def stock_data_viz_view(request):
    stock_data = JsonModel.objects.all().values()
    df = pd.DataFrame(stock_data)
    df['date'] = pd.to_datetime(df['date'])


    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    df["trade_code"] = df['trade_code'].astype(str)


    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['open'] = df['open'].astype(float)
    df['close'] = df['close'].astype(float)
    df['volume'] = df['volume'].astype(float)


    data_for_d3 = df[['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']].to_dict(orient='records')
    context = {'data_for_d3': data_for_d3}

    return render(request, 'stockapp/stock_data_vizo.html', context)

def stock_data_list(request):
    stock_data = SqlModel.objects.all().values()
    df = pd.DataFrame(stock_data)
    df1 = df.date.tolist()
    df2 = df.trade_code.tolist()
    df3 = df.high.tolist()
    df4 = df.low.tolist()
    df5 = df.open.tolist()
    df6 = df.close.tolist()
    df7 = df.volume.tolist()
    return render(request, 'stockapp/stock_data_list.html', {'stock_data': stock_data})

def stock_data_detail(request, id):
    obj = get_object_or_404(SqlModel, pk=id)
    return render(request, 'stockapp/stock_data_detail.html', {'obj': obj})


def stock_data_create(request):
    if request.method == 'POST':
        form = SqlModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_data_list')
    else:
        form = SqlModelForm()
    return render(request, 'stockapp/stock_data_form.html', {'form': form})


def stock_data_update(request, id):
    obj = get_object_or_404(SqlModel, pk=id)
    if request.method == 'POST':
        form = SqlModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('stock_data_list')
    else:
        form = SqlModelForm(instance=obj)
    return render(request, 'stockapp/stock_data_form.html', {'form': form})


def stock_data_delete(request, id):
    obj = get_object_or_404(SqlModel, pk=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('stock_data_list')
    return render(request, 'stockapp/stock_data_confirm_delete.html', {'obj': obj})

