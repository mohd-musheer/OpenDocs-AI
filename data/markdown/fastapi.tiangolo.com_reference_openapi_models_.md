
# OpenAPI models - FastAPI

URL: https://fastapi.tiangolo.com/reference/openapi/models/

OpenAPI models
¶
OpenAPI Pydantic models used to generate and validate the generated OpenAPI.
fastapi.openapi.models
¶
SchemaType
module-attribute
¶
SchemaType = Literal[
"array",
"boolean",
"integer",
"null",
"number",
"object",
"string",
]
SecurityScheme
module-attribute
¶
SecurityScheme = (
APIKey | HTTPBase | OAuth2 | OpenIdConnect | HTTPBearer
)
BaseModelWithConfig
¶
Bases: BaseModel
Contact
¶
Bases: BaseModelWithConfig
License
¶
Bases: BaseModelWithConfig
Info
¶
Bases: BaseModelWithConfig
ServerVariable
¶
Bases: BaseModelWithConfig
Server
¶
Bases: BaseModelWithConfig
Discriminator
¶
XML
¶
Bases: BaseModelWithConfig
ExternalDocumentation
¶
Bases: BaseModelWithConfig
Schema
¶
Bases: BaseModelWithConfig
vocabulary
class-attribute
instance-attribute
¶
vocabulary = Field(default=None, alias='$vocabulary')
dynamicAnchor
class-attribute
instance-attribute
¶
dynamicAnchor = Field(default=None, alias='$dynamicAnchor')
dynamicRef
class-attribute
instance-attribute
¶
dynamicRef = Field(default=None, alias='$dynamicRef')
example
class-attribute
instance-attribute
¶
example = None
Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
Example
¶
ParameterInType
¶
Encoding
¶
Bases: BaseModelWithConfig
MediaType
¶
Bases: BaseModelWithConfig
ParameterBase
¶
Bases: BaseModelWithConfig
Parameter
¶
Bases: ParameterBase
Header
¶
Bases: ParameterBase
RequestBody
¶
Bases: BaseModelWithConfig
Link
¶
Bases: BaseModelWithConfig
Response
¶
Bases: BaseModelWithConfig
Operation
¶
Bases: BaseModelWithConfig
PathItem
¶
Bases: BaseModelWithConfig
SecuritySchemeType
¶
SecurityBase
¶
Bases: BaseModelWithConfig
APIKeyIn
¶
APIKey
¶
Bases: SecurityBase
HTTPBase
¶
OAuthFlow
¶
Bases: BaseModelWithConfig
OAuthFlowImplicit
¶
OAuthFlowPassword
¶
OAuthFlowClientCredentials
¶
OAuthFlows
¶
Bases: BaseModelWithConfig
OAuth2
¶
OpenIdConnect
¶
Bases: SecurityBase
Components
¶
Bases: BaseModelWithConfig
Tag
¶
Bases: BaseModelWithConfig
OpenAPI
¶
Bases: BaseModelWithConfig
