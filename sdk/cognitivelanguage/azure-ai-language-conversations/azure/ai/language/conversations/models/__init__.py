# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AgeResolution
from ._models import AnalysisParameters
from ._models import AnalyzeConversationResult
from ._models import AnalyzeConversationTask
from ._models import AnalyzeConversationTaskResult
from ._models import AnswerSpan
from ._models import AreaResolution
from ._models import BaseExtraInformation
from ._models import BasePrediction
from ._models import BaseResolution
from ._models import BooleanResolution
from ._models import ConversationAnalysisOptions
from ._models import ConversationCallingOptions
from ._models import ConversationEntity
from ._models import ConversationIntent
from ._models import ConversationItemBase
from ._models import ConversationParameters
from ._models import ConversationPrediction
from ._models import ConversationResult
from ._models import ConversationTargetIntentResult
from ._models import CurrencyResolution
from ._models import CustomConversationTaskParameters
from ._models import CustomConversationalTask
from ._models import CustomConversationalTaskResult
from ._models import DateTimeResolution
from ._models import EntitySubtype
from ._models import Error
from ._models import ErrorResponse
from ._models import InformationResolution
from ._models import InnerErrorModel
from ._models import KnowledgeBaseAnswer
from ._models import KnowledgeBaseAnswerDialog
from ._models import KnowledgeBaseAnswerPrompt
from ._models import KnowledgeBaseAnswers
from ._models import LUISCallingOptions
from ._models import LUISParameters
from ._models import LUISTargetIntentResult
from ._models import LengthResolution
from ._models import ListKey
from ._models import NoneLinkedTargetIntentResult
from ._models import NumberResolution
from ._models import NumericRangeResolution
from ._models import OrchestratorPrediction
from ._models import OrdinalResolution
from ._models import QuantityResolution
from ._models import QuestionAnsweringParameters
from ._models import QuestionAnsweringTargetIntentResult
from ._models import SpeedResolution
from ._models import TargetIntentResult
from ._models import TemperatureResolution
from ._models import TemporalSpanResolution
from ._models import TextConversationItem
from ._models import VolumeResolution
from ._models import WeightResolution


from ._enums import (
    AgeUnit,
    AnalyzeConversationTaskKind,
    AnalyzeConversationTaskResultsKind,
    AreaUnit,
    DateTimeSubKind,
    ErrorCode,
    ExtraInformationKind,
    InformationUnit,
    InnerErrorCode,
    LengthUnit,
    Modality,
    Modifier,
    NumberKind,
    ProjectKind,
    RangeKind,
    RelativeTo,
    ResolutionKind,
    SpeedUnit,
    TargetKind,
    TemperatureUnit,
    VolumeUnit,
    WeightUnit,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AgeResolution',
    'AnalysisParameters',
    'AnalyzeConversationResult',
    'AnalyzeConversationTask',
    'AnalyzeConversationTaskResult',
    'AnswerSpan',
    'AreaResolution',
    'BaseExtraInformation',
    'BasePrediction',
    'BaseResolution',
    'BooleanResolution',
    'ConversationAnalysisOptions',
    'ConversationCallingOptions',
    'ConversationEntity',
    'ConversationIntent',
    'ConversationItemBase',
    'ConversationParameters',
    'ConversationPrediction',
    'ConversationResult',
    'ConversationTargetIntentResult',
    'CurrencyResolution',
    'CustomConversationTaskParameters',
    'CustomConversationalTask',
    'CustomConversationalTaskResult',
    'DateTimeResolution',
    'EntitySubtype',
    'Error',
    'ErrorResponse',
    'InformationResolution',
    'InnerErrorModel',
    'KnowledgeBaseAnswer',
    'KnowledgeBaseAnswerDialog',
    'KnowledgeBaseAnswerPrompt',
    'KnowledgeBaseAnswers',
    'LUISCallingOptions',
    'LUISParameters',
    'LUISTargetIntentResult',
    'LengthResolution',
    'ListKey',
    'NoneLinkedTargetIntentResult',
    'NumberResolution',
    'NumericRangeResolution',
    'OrchestratorPrediction',
    'OrdinalResolution',
    'QuantityResolution',
    'QuestionAnsweringParameters',
    'QuestionAnsweringTargetIntentResult',
    'SpeedResolution',
    'TargetIntentResult',
    'TemperatureResolution',
    'TemporalSpanResolution',
    'TextConversationItem',
    'VolumeResolution',
    'WeightResolution',
    'AgeUnit',
    'AnalyzeConversationTaskKind',
    'AnalyzeConversationTaskResultsKind',
    'AreaUnit',
    'DateTimeSubKind',
    'ErrorCode',
    'ExtraInformationKind',
    'InformationUnit',
    'InnerErrorCode',
    'LengthUnit',
    'Modality',
    'Modifier',
    'NumberKind',
    'ProjectKind',
    'RangeKind',
    'RelativeTo',
    'ResolutionKind',
    'SpeedUnit',
    'TargetKind',
    'TemperatureUnit',
    'VolumeUnit',
    'WeightUnit',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()