import abc
import importlib


class Plugins(abc.ABCMeta):
    plugins = dict()

    def __new__(metaclass, name, bases, namespace):
        cls = abc.ABCMeta.__new__(metaclass, name, bases, namespace)

        if isinstance(cls.name, str):
            metaclass.plugins[cls.name] = cls

        return cls

    @classmethod
    def get(cls, name):
        if name not in cls.plugins:
            print('Loading plugins from plugins.%s' % name)
            importlib.import_module('plugins.%s' % name)
        return cls.plugins[name]


class PluginBase(metaclass=Plugins):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()


class SpamPlugin(PluginBase):
    name = 'spam'


class EggsPlugin(PluginBase):
    name = 'eggs'


print(EggsPlugin().name)
print(Plugins.plugins)
