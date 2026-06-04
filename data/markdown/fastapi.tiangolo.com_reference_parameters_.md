
# Request Parameters - FastAPI

URL: https://fastapi.tiangolo.com/reference/parameters/

Request Parameters¶
Here's the reference information for the request parameters.
These are the special functions that you can put in path operation function parameters or dependency functions with Annotated
to get data from the request.
It includes:
Query()
Path()
Body()
Cookie()
Header()
Form()
File()
You can import them all directly from fastapi
:
from fastapi import Body, Cookie, File, Form, Header, Path, Query
fastapi.Query
¶
Query(
default=Undefined,
*,
default_factory=_Unset,
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
description
|
Human-readable description. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
min_length
|
Minimum length for strings. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
max_length
|
Maximum length for strings. Read more about it in the FastAPI docs about Query parameters
TYPE:
|
pattern
|
RegEx pattern for strings. Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at Read more about it in the FastAPI docs about Query parameters
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at Read more about it in the [FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Query( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alternative-old-query-as-the-default-value)
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alias-parameters)
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata)
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata)
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#add-regular-expressions
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#deprecating-parameters)
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
Read more about it in the
[FastAPI docs about Query parameters](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.Query(
default=default,
default_factory=default_factory,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.Path
¶
Path(
default=...,
*,
default_factory=_Unset,
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
Declare a path parameter for a path operation.
Read more about it in the FastAPI docs for Path Parameters and Numeric Validations.
from typing import Annotated
from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/items/{item_id}")
async def read_items(
item_id: Annotated[int, Path(title="The ID of the item to get")],
):
return {"item_id": item_id}
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set. This doesn't affect
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title. Read more about it in the FastAPI docs for Path Parameters and Numeric Validations
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. Read more about it in the FastAPI docs about Path parameters numeric validations
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Path( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = ...,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
Read more about it in the
[FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata)
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
Read more about it in the
[FastAPI docs about Path parameters numeric validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#number-validations-greater-than-and-less-than-or-equal)
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
"""
Declare a path parameter for a *path operation*.
Read more about it in the
[FastAPI docs for Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/).
```python
from typing import Annotated
from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/items/{item_id}")
async def read_items(
item_id: Annotated[int, Path(title="The ID of the item to get")],
):
return {"item_id": item_id}
```
"""
return params.Path(
default=default,
default_factory=default_factory,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.Body
¶
Body(
default=Undefined,
*,
default_factory=_Unset,
embed=None,
media_type="application/json",
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set.
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
embed
|
When This happens automatically when more than one Read more about it in the FastAPI docs for Body - Multiple Parameters.
TYPE:
|
media_type
|
The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data.
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title.
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers.
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers.
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Body( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
embed: Annotated[
bool | None,
Doc(
"""
When `embed` is `True`, the parameter will be expected in a JSON body as a
key instead of being the JSON body itself.
This happens automatically when more than one `Body` parameter is declared.
Read more about it in the
[FastAPI docs for Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter).
"""
),
] = None,
media_type: Annotated[
str,
Doc(
"""
The media type of this parameter field. Changing it would affect the
generated OpenAPI, but currently it doesn't affect the parsing of the data.
"""
),
] = "application/json",
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.Body(
default=default,
default_factory=default_factory,
embed=embed,
media_type=media_type,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.Cookie
¶
Cookie(
default=Undefined,
*,
default_factory=_Unset,
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set.
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title.
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers.
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers.
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Cookie( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.Cookie(
default=default,
default_factory=default_factory,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.Header
¶
Header(
default=Undefined,
*,
default_factory=_Unset,
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
convert_underscores=True,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set.
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
convert_underscores
|
Automatically convert underscores to hyphens in the parameter field name. Read more about it in the FastAPI docs for Header Parameters
TYPE:
|
title
|
Human-readable title.
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers.
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers.
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Header( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
convert_underscores: Annotated[
bool,
Doc(
"""
Automatically convert underscores to hyphens in the parameter field name.
Read more about it in the
[FastAPI docs for Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion)
"""
),
] = True,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.Header(
default=default,
default_factory=default_factory,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
convert_underscores=convert_underscores,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.Form
¶
Form(
default=Undefined,
*,
default_factory=_Unset,
media_type="application/x-www-form-urlencoded",
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set.
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
media_type
|
The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data.
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title.
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers.
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers.
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def Form( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
media_type: Annotated[
str,
Doc(
"""
The media type of this parameter field. Changing it would affect the
generated OpenAPI, but currently it doesn't affect the parsing of the data.
"""
),
] = "application/x-www-form-urlencoded",
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.Form(
default=default,
default_factory=default_factory,
media_type=media_type,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
fastapi.File
¶
File(
default=Undefined,
*,
default_factory=_Unset,
media_type="multipart/form-data",
alias=None,
alias_priority=_Unset,
validation_alias=None,
serialization_alias=None,
title=None,
description=None,
gt=None,
ge=None,
lt=None,
le=None,
min_length=None,
max_length=None,
pattern=None,
regex=None,
discriminator=None,
strict=_Unset,
multiple_of=_Unset,
allow_inf_nan=_Unset,
max_digits=_Unset,
decimal_places=_Unset,
examples=None,
example=_Unset,
openapi_examples=None,
deprecated=None,
include_in_schema=True,
json_schema_extra=None,
**extra
)
| PARAMETER | DESCRIPTION |
|---|---|
default
|
Default value if the parameter field is not set.
TYPE:
|
default_factory
|
A callable to generate the default value. This doesn't affect
TYPE:
|
media_type
|
The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data.
TYPE:
|
alias
|
An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.
TYPE:
|
alias_priority
|
Priority of the alias. This affects whether an alias generator is used.
TYPE:
|
validation_alias
|
'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.
TYPE:
|
serialization_alias
|
'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.
TYPE:
|
title
|
Human-readable title.
TYPE:
|
description
|
Human-readable description.
TYPE:
|
gt
|
Greater than. If set, value must be greater than this. Only applicable to numbers.
TYPE:
|
ge
|
Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
TYPE:
|
lt
|
Less than. If set, value must be less than this. Only applicable to numbers.
TYPE:
|
le
|
Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
TYPE:
|
min_length
|
Minimum length for strings.
TYPE:
|
max_length
|
Maximum length for strings.
TYPE:
|
pattern
|
RegEx pattern for strings.
TYPE:
|
regex
|
Deprecated in FastAPI 0.100.0 and Pydantic v2, use
TYPE:
|
discriminator
|
Parameter field name for discriminating the type in a tagged union.
TYPE:
|
strict
|
If
TYPE:
|
multiple_of
|
Value must be a multiple of this. Only applicable to numbers.
TYPE:
|
allow_inf_nan
|
Allow
TYPE:
|
max_digits
|
Maximum number of digits allowed for decimal values.
TYPE:
|
decimal_places
|
Maximum number of decimal places allowed for decimal values.
TYPE:
|
examples
|
Example values for this field. Read more about it in the FastAPI docs for Declare Request Example Data
TYPE:
|
example
|
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
TYPE:
|
openapi_examples
|
OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at Swagger UI (that provides the Read more about it in the FastAPI docs for Declare Request Example Data. |
deprecated
|
Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at
TYPE:
|
include_in_schema
|
To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at
TYPE:
|
json_schema_extra
|
Any additional JSON schema data.
TYPE:
|
**extra
|
The
TYPE:
|
Source code in fastapi/param_functions.py
def File( # noqa: N802
default: Annotated[
Any,
Doc(
"""
Default value if the parameter field is not set.
"""
),
] = Undefined,
*,
default_factory: Annotated[
Callable[[], Any] | None,
Doc(
"""
A callable to generate the default value.
This doesn't affect `Path` parameters as the value is always required.
The parameter is available only for compatibility.
"""
),
] = _Unset,
media_type: Annotated[
str,
Doc(
"""
The media type of this parameter field. Changing it would affect the
generated OpenAPI, but currently it doesn't affect the parsing of the data.
"""
),
] = "multipart/form-data",
alias: Annotated[
str | None,
Doc(
"""
An alternative name for the parameter field.
This will be used to extract the data and for the generated OpenAPI.
It is particularly useful when you can't use the name you want because it
is a Python reserved keyword or similar.
"""
),
] = None,
alias_priority: Annotated[
int | None,
Doc(
"""
Priority of the alias. This affects whether an alias generator is used.
"""
),
] = _Unset,
validation_alias: Annotated[
str | AliasPath | AliasChoices | None,
Doc(
"""
'Whitelist' validation step. The parameter field will be the single one
allowed by the alias or set of aliases defined.
"""
),
] = None,
serialization_alias: Annotated[
str | None,
Doc(
"""
'Blacklist' validation step. The vanilla parameter field will be the
single one of the alias' or set of aliases' fields and all the other
fields will be ignored at serialization time.
"""
),
] = None,
title: Annotated[
str | None,
Doc(
"""
Human-readable title.
"""
),
] = None,
description: Annotated[
str | None,
Doc(
"""
Human-readable description.
"""
),
] = None,
gt: Annotated[
float | None,
Doc(
"""
Greater than. If set, value must be greater than this. Only applicable to
numbers.
"""
),
] = None,
ge: Annotated[
float | None,
Doc(
"""
Greater than or equal. If set, value must be greater than or equal to
this. Only applicable to numbers.
"""
),
] = None,
lt: Annotated[
float | None,
Doc(
"""
Less than. If set, value must be less than this. Only applicable to numbers.
"""
),
] = None,
le: Annotated[
float | None,
Doc(
"""
Less than or equal. If set, value must be less than or equal to this.
Only applicable to numbers.
"""
),
] = None,
min_length: Annotated[
int | None,
Doc(
"""
Minimum length for strings.
"""
),
] = None,
max_length: Annotated[
int | None,
Doc(
"""
Maximum length for strings.
"""
),
] = None,
pattern: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
] = None,
regex: Annotated[
str | None,
Doc(
"""
RegEx pattern for strings.
"""
),
deprecated(
"Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
),
] = None,
discriminator: Annotated[
str | None,
Doc(
"""
Parameter field name for discriminating the type in a tagged union.
"""
),
] = None,
strict: Annotated[
bool | None,
Doc(
"""
If `True`, strict validation is applied to the field.
"""
),
] = _Unset,
multiple_of: Annotated[
float | None,
Doc(
"""
Value must be a multiple of this. Only applicable to numbers.
"""
),
] = _Unset,
allow_inf_nan: Annotated[
bool | None,
Doc(
"""
Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
"""
),
] = _Unset,
max_digits: Annotated[
int | None,
Doc(
"""
Maximum number of digits allowed for decimal values.
"""
),
] = _Unset,
decimal_places: Annotated[
int | None,
Doc(
"""
Maximum number of decimal places allowed for decimal values.
"""
),
] = _Unset,
examples: Annotated[
list[Any] | None,
Doc(
"""
Example values for this field.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
"""
),
] = None,
example: Annotated[
Any | None,
deprecated(
"Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
"although still supported. Use examples instead."
),
] = _Unset,
openapi_examples: Annotated[
dict[str, Example] | None,
Doc(
"""
OpenAPI-specific examples.
It will be added to the generated OpenAPI (e.g. visible at `/docs`).
Swagger UI (that provides the `/docs` interface) has better support for the
OpenAPI-specific examples than the JSON Schema `examples`, that's the main
use case for this.
Read more about it in the
[FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
"""
),
] = None,
deprecated: Annotated[
deprecated | str | bool | None,
Doc(
"""
Mark this parameter field as deprecated.
It will affect the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = None,
include_in_schema: Annotated[
bool,
Doc(
"""
To include (or not) this parameter field in the generated OpenAPI.
You probably don't need it, but it's available.
This affects the generated OpenAPI (e.g. visible at `/docs`).
"""
),
] = True,
json_schema_extra: Annotated[
dict[str, Any] | None,
Doc(
"""
Any additional JSON schema data.
"""
),
] = None,
**extra: Annotated[
Any,
Doc(
"""
Include extra fields used by the JSON Schema.
"""
),
deprecated(
"""
The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
"""
),
],
) -> Any:
return params.File(
default=default,
default_factory=default_factory,
media_type=media_type,
alias=alias,
alias_priority=alias_priority,
validation_alias=validation_alias,
serialization_alias=serialization_alias,
title=title,
description=description,
gt=gt,
ge=ge,
lt=lt,
le=le,
min_length=min_length,
max_length=max_length,
pattern=pattern,
regex=regex,
discriminator=discriminator,
strict=strict,
multiple_of=multiple_of,
allow_inf_nan=allow_inf_nan,
max_digits=max_digits,
decimal_places=decimal_places,
example=example,
examples=examples,
openapi_examples=openapi_examples,
deprecated=deprecated,
include_in_schema=include_in_schema,
json_schema_extra=json_schema_extra,
**extra,
)
