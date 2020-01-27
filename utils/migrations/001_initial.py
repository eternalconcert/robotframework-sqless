old_state = {}

actions = {'creations': {'Post': {'fields': [{'title': {'field_attrs': {'max_length': 100},
                                              'field_type': 'CharField'}},
                                   {'content': {'field_attrs': {},
                                                'field_type': 'TextField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'post'},
               'User': {'fields': [{'username': {'field_attrs': {'max_length': 20},
                                                 'field_type': 'CharField'}},
                                   {'email': {'field_attrs': {'max_length': 100},
                                              'field_type': 'CharField'}},
                                   {'failed_logins': {'field_attrs': {'default': 0},
                                                      'field_type': 'IntegerField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'user'}}}

new_state = {'Post': {'fields': [{'title': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'content': {'field_attrs': {},
                                  'field_type': 'TextField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'post'},
 'User': {'fields': [{'username': {'field_attrs': {'max_length': 20},
                                   'field_type': 'CharField'}},
                     {'email': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'failed_logins': {'field_attrs': {'default': 0},
                                        'field_type': 'IntegerField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}

