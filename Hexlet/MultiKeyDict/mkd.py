class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.

        """
        # BEGIN (write your solution here)
        self._sequence = 0
        self._keys = {}
        self._values = {}
        for k, v in kwargs.items():
            self[k] = v

        # END

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.

        """
        # BEGIN (write your solution here)
        return self._values[self._keys[key]]
        # END

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.

        """
        internal_key = self._keys.get(key)
        if internal_key is None:
            self._sequence += 1
            internal_key = self._sequence
            self._keys[key] = internal_key
        self._values[internal_key] = value

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.

        """
        # BEGIN (write your solution here)
        for new_key, key in kwargs.items():
            self._keys[new_key] = self._keys[key]
            # Текущая реализация позволяет делать существующие ключи
            # псевдонимами для других существующих ключей.
            # Это может привести к "осиротению" некоторых значений —
            # значения могут потерять внешний ключ. Такие "сироты"
            # будут занимать память, но не будут доступны извне.
            # В реальном коде эту проблему пришлось бы решать,
            # для учебных же целей реализация годится и в таком виде.
        # END
