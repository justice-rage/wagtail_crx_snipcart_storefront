from website.models import (
    ProductsIndexPage, 
    ProductsPage, 
    SnipcartSettings
)

# ------ E-Commerce Section: Snipcart Pages ------

class ProductsIndexPage:
    class Meta:
        verbose_name = "Products Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'testapp.ProductsPage'

    # Only allow ProductsPages beneath this page.
    subpage_types = ['testapp.ProductsPage']

    # template = 'website/pages/products_index_page.html'
    template = 'coderedcms/pages/products_index_page.html'

class ProductsPage:
    class Meta:
        verbose_name = "Products Page"

    # Only allow this page to be created beneath an ProductsIndexPage.
    parent_page_types = ['testapp.ProductsIndexPage']

    # template = "website/pages/products_page.html"
    template = "coderedcms/pages/products_page.html"

# ------ Snipcart Configuration Settings ------

class SnipcartSettings:
    class Meta:
        verbose_name = ("Snipcart")
        # verbose_name = _("Snipcart")

    # snipcart_api_key = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     verbose_name=_("Snipcart API Key"),
    #     help_text=_("The API Key used for Snipcart."),
    # )