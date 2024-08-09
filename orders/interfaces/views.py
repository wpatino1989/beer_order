from django.http import JsonResponse
from django.core.exceptions import ValidationError
from orders.infrastructure.repositories import JsonOrderRepository, JsonStockRepository
from orders.application.services import OrderService, StockService

order_service = OrderService(order_repository=JsonOrderRepository())
stock_service = StockService(stock_repository=JsonStockRepository())

def order_status(request):
    try:
        order = order_service.get_order_status()
        return JsonResponse({
                'status': 'success',
                'data': order.to_dict()
            }, status=200)
    except ValidationError as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Internal Server Error'
        }, status=500)

def stock_status(request):
    try:
        stock = stock_service.get_stock()        
    except ValidationError as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Internal Server Error'
        }, status=500)

    return JsonResponse(stock, safe=False)
