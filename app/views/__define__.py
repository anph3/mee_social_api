import os
import jwt
import bcrypt
import uuid
from datetime import datetime

# ========== include rest_framework ==========
from rest_framework.viewsets import ViewSet
# =============== end include  ===============

# =============== validate  ===============
from ..validations.auth_validate import *
# =============== end validate  ===============

from ..serializers.user_serializer import *

from helpers import response as rs
from helpers import helper as hp

from configs import variable_response as vr
from configs import variable_system as vs

from django.db.models import Q
from django.core.cache import cache