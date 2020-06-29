from oscar.apps.shipping import repository
from . import methods as shipping_methods

'''
class Repository(repository.Repository):

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        methods = (shipping_methods.Standard(),)
        if shipping_addr and shipping_addr.country.code == 'GB':
            # Express is only available in the UK
            methods = (shipping_methods.Standard(), shipping_methods.Express())
        return methods


'''