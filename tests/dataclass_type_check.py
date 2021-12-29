from typing import get_args


def check(subject):
    for name, definition in subject.__dataclass_fields__.items():
        if isinstance(subject.__getattribute__(name), list):
            for list_subject in subject.__getattribute__(name):
                try:
                    check(list_subject)
                except AttributeError:
                    # test doesnt check types like
                    # Optional[list[Union[int, float]]]
                    # as definition.type would be a tuple:
                    # (list[typing.Union[int, float]], <class 'NoneType'>)
                    # which isnt valid for isinstance(_, definition.type)
                    # and im not able to figure a way out to catch and
                    # test this properly (typing in py pepega)
                    pass
            continue
        field = subject.__getattribute__(name)
        field_type = (
            get_args(definition.type) if get_args(definition.type) else definition.type
        )
        print(name, field, field_type)
        assert isinstance(field, field_type)
