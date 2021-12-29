from typing import get_args


def check(subject):
    for name, definition in subject.__dataclass_fields__.items():
        if isinstance(subject.__getattribute__(name), list):
            for list_subject in subject.__getattribute__(name):
                check(list_subject)
            continue
        field = subject.__getattribute__(name)
        field_type = (
            get_args(definition.type) if get_args(definition.type) else definition.type
        )
        print(field, field_type)
        assert isinstance(field, field_type)
