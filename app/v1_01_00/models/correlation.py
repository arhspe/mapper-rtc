from pydantic import BaseModel, Field
from typing import List

class NbsService(BaseModel):
    nbs: str = Field(..., example="1.1502.10.00", description="Código da NBS")
    descricao_nbs: str = Field(..., example="Serviços de projeto, desenvolvimento...", description="Descrição da atividade na NBS")

class TaxClassification(BaseModel):
  
    cClassTrib: str = Field(..., example="000001", description="Código de Classificação Tributária")
    nome_cClassTrib: str = Field(..., example="Situações tributadas integralmente...", description="Nome da classificação tributária")

class OperationParameters(BaseModel):
    ps_onerosa: str = Field(..., example="S", description="Prestação de Serviço Onerosa (S/N)")
    adq_exterior: str = Field(..., example="N", description="Adquiriu no Exterior (S/N)")
    cIndOp: str = Field(..., example="100301", description="Indicador de Operação")
    local_incidencia_ibs: str = Field(..., example="Domicílio principal do adquirente", description="Regra de local de incidência do IBS")

class CorrelationResponse(BaseModel):
    item_lc_116: str = Field(..., example="01.01", description="Código do item da Lei Complementar 116/2003")
    descricao_item: str = Field(..., example="Análise E Desenvolvimento De Sistemas.", description="Descrição oficial do item da LC 116")
    parametros_operacao: OperationParameters = Field(..., description="Parâmetros fiscais da operação")
    servicos_nbs: List[NbsService] = Field(..., description="Lista de serviços NBS vinculados")
    classificacoes_tributarias: List[TaxClassification] = Field(..., description="Classificações tributárias aplicáveis")