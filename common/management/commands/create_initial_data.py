from django.core.management.base import BaseCommand
from common.models import Location, Department, Category, SubCategory, SKU

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        # Define data
        locations = ['Perimeter', 'Center']
        departments = {
            'Perimeter': ['Bakery', 'Deli and Foodservice', 'Floral', 'Seafood'],
            'Center': ['Dairy', 'Frozen', 'GM', 'Grocery']
        }
        categories = {
            'Bakery': ['Bakery Bread', 'In Store Bakery'],
            'Deli and Foodservice': ['Self Service Deli Cold', 'Service Deli'],
            'Floral': ['Bouquets and Cut Flowers', 'Gifts', 'Plants'],
            'Seafood': ['Frozen Shellfish', 'Other Seafood'],
            'Dairy': ['Cheese', 'Cream or Creamer', 'Cultured', 'Refrigerated Baking'],
            'Frozen': ['Frozen Bake', 'Frozen Breakfast', 'Frozen Desserts or Fruit and Toppings', 'Frozen Juice'],
            'GM': ['Audio Video', 'Housewares', 'Insect and Rodent', 'Kitchen Accessories', 'Laundry'],
            'Grocery': ['Baking Ingredients', 'Spices', 'Stuffing Products']
        }
        subcategories = {
            'Bakery Bread': ['Bagels', 'Baking or Breading Products', 'English Muffins or Biscuits', 'Flatbreads'],
            'In Store Bakery': ['Breakfast Cake or Sweet Roll', 'Cakes', 'Pies', 'Seasonal'],
            'Self Service Deli Cold': ['Beverages'],
            'Service Deli': ['Cheese All Other', 'Cheese American'],
            'Bouquets and Cut Flowers': ['Bouquets and Cut Flowers'],
            'Gifts': ['Gifts'],
            'Plants': ['Plants'],
            'Frozen Shellfish': ['Frozen Shellfish'],
            'Other Seafood': ['All Other Seafood', 'Prepared Seafood Entrees', 'Seafood Salads', 'Smoked Fish', 'Seafood Breading Sauces Dips'],
            'Cheese': ['Cheese Sauce', 'Specialty Cheese'],
            'Cream or Creamer': ['Dairy Alternative Creamer', 'Whipping Creams'],
            'Cultured': ['Cottage Cheese'],
            'Refrigerated Baking': ['Refrigerated Breads', 'Refrigerated English Muffins and Biscuits', 'Refrigerated Hand Held Sweets', 'Refrigerated Pie Crust', 'Refrigerated Sweet Breakfast Baked Goods'],
            'Frozen Bake': ['Bread or Dough Products Frozen', 'Breakfast Cake or Sweet Roll Frozen'],
            'Frozen Breakfast': ['Frozen Breakfast Entrees', 'Frozen Breakfast Sandwich', 'Frozen Egg Substitutes', 'Frozen Syrup Carriers'],
            'Frozen Desserts or Fruit and Toppings': ['Pies Frozen'],
            'Frozen Juice': ['Frozen Apple Juice', 'Frozen Fruit Drink Mixers', 'Frozen Fruit Juice All Other'],
            'Audio Video': ['Audio', 'Video DVD', 'Video VHS'],
            'Housewares': ['Bedding', 'Candles', 'Collectibles and Gifts', 'Flashlights', 'Frames'],
            'Insect and Rodent': ['Indoor Repellants or Traps', 'Outdoor Repellants or Traps'],
            'Kitchen Accessories': ['Kitchen Accessories'],
            'Laundry': ['Bleach Liquid', 'Bleach Powder', 'Fabric Softener Liquid', 'Fabric Softener Sheets'],
            'Baking Ingredients': ['Dry or Canned Milk', 'Food Coloring'],
            'Spices': ['Salt Cooking or Edible or Seasoned', 'Salt Substitute', 'Seasoning Dry'],
            'Stuffing Products': ['Stuffing Products']
        }

        # Populate Locations
        for loc in locations:
            location = Location.objects.get_or_create(name=loc)[0]
            for dep in departments[loc]:
                department = Department.objects.get_or_create(name=dep, location=location)[0]
                for cat in categories[dep]:
                    category = Category.objects.get_or_create(name=cat, department=department)[0]
                    for subcat in subcategories[cat]:
                        SubCategory.objects.get_or_create(name=subcat, category=category)[0]

        # Populate SKUs
        skus = [
            ('SKUDESC1', 'Perimeter', 'Bakery', 'Bakery Bread', 'Bagels'),
            ('SKUDESC2', 'Perimeter', 'Deli and Foodservice', 'Self Service Deli Cold', 'Beverages'),
            ('SKUDESC3', 'Perimeter', 'Floral', 'Bouquets and Cut Flowers', 'Bouquets and Cut Flowers'),
            ('SKUDESC4', 'Perimeter', 'Deli and Foodservice', 'Service Deli', 'All Other'),
            ('SKUDESC5', 'Center', 'Frozen', 'Frozen Bake', 'Bread or Dough Products Frozen'),
            ('SKUDESC6', 'Center', 'Grocery', 'Crackers', 'Rice Cakes'),
            ('SKUDESC7', 'Center', 'GM', 'Audio Video', 'Audio'),
            ('SKUDESC8', 'Center', 'GM', 'Audio Video', 'Video DVD'),
            ('SKUDESC9', 'Perimeter', 'GM', 'Housewares', 'Bedding'),
            ('SKUDESC10', 'Perimeter', 'Seafood', 'Frozen Shellfish', 'Frozen Shellfish'),
            ('SKUDESC11', 'Perimeter', 'Seafood', 'Other Seafood', 'All Other Seafood'),
            ('SKUDESC12', 'Perimeter', 'Seafood', 'Other Seafood', 'Prepared Seafood Entrees'),
            ('SKUDESC13', 'Perimeter', 'Seafood', 'Other Seafood', 'Seafood Salads'),
            ('SKUDESC14', 'Perimeter', 'Bakery', 'Bakery Bread', 'Bagels'),
            ('SKUDESC15', 'Perimeter', 'Deli and Foodservice', 'Self Service Deli Cold', 'Beverages'),
            ('SKUDESC16', 'Perimeter', 'Floral', 'Bouquets and Cut Flowers', 'Bouquets and Cut Flowers'),
            ('SKUDESC17', 'Perimeter', 'Deli and Foodservice', 'Service Deli', 'All Other'),
            ('SKUDESC18', 'Center', 'Frozen', 'Frozen Bake', 'Bread or Dough Products Frozen'),
        ]

        for name, loc, dep, cat, subcat in skus:
            location = Location.objects.filter(name=loc).first()
            department = Department.objects.filter(name=dep, location=location).first()
            category = Category.objects.filter(name=cat, department=department).first()
            subcategory = SubCategory.objects.filter(name=subcat, category=category).first()
            if any((location, department, category, subcategory)):
                SKU.objects.get_or_create(name=name, location=location, department=department, category=category, subcategory=subcategory)
