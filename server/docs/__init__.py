def param(name, description, required=True, in_data='json', type='str'):
    return {
        'name': name,
        'description': description,
        'in': in_data,
        'type': type,
        'required': required
    }


jwt_header = param('Authorization', 'JWT Token', in_data='header')
