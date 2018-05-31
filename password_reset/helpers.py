import importlib

def get_form_class(class_path):
	module_path = '.'.join(class_path.split('.')[:-1])
	class_name = class_path.split('.')[-1]
	module = importlib.import_module(module_path)
	return getattr(module, class_name)