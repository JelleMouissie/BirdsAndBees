

def make_getter(name):
    """Returns a getter function which returns the attribute `name'."""
    return lambda self: getattr(self, name)
def make_setter(name, var_type, user_setter):
    """Returns a setter function which sets the attribute `name', first casting
    it to `type' and passing it through the `user_setter' function."""
    return lambda self, new_val: setattr(self, name,
            user_setter(var_type(new_val)))

class Model(object):
    def __init__(self):
        self.params = []

    def reset(self):
        raise Exception("Override the `reset' method in your model class.")

    def step(self):
        raise Exception("Override the `step' method in your model class.")

    def draw(self):
        raise Exception("Override the `draw' method in your model class.")

    def make_param(self, name, default_value, param_type=None, setter=None):
        setter = setter or (lambda x: x)
        param_type = param_type or type(default_value)
        hidden_var_name = '_param_%s' % name
        self.params.append(name)
        setattr(self, hidden_var_name, setter(param_type(default_value)))
        setattr(self.__class__, name,
                property(make_getter(hidden_var_name),
                         make_setter(hidden_var_name, param_type, setter)))
