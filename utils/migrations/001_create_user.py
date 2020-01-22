old_state = {}

actions = {'creations': {'User': {'fields': [{'username': {'field_attrs': {'max_length': 20},
                                                 'field_type': 'CharField'}},
                                   {'email': {'field_attrs': {'max_length': 100},
                                              'field_type': 'CharField'}},
                                   {'failed_logins': {'field_attrs': {'default': 0},
                                                      'field_type': 'IntegerField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'user'}}}

new_state = {'User': {'fields': [{'username': {'field_attrs': {'max_length': 20},
                                   'field_type': 'CharField'}},
                     {'email': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'failed_logins': {'field_attrs': {'default': 0},
                                        'field_type': 'IntegerField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}

