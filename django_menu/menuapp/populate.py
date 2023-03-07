from menuapp.models import Menu, MenuNode


m = Menu.objects.create(name='main', slug='main_menu')
MenuNode.objects.create(menu=m, value='Node0', named_url='from_Node0')
Node1 = MenuNode.objects.create(menu=m, value='Node1', named_url='from_Node1')
Node1A = MenuNode.objects.create(value='Node1A', parent=Node1,)
MenuNode.objects.create(value='Node2A', parent=Node1, named_url='from_Node2A')
MenuNode.objects.create(value='Node1AX', parent=Node1A,)
