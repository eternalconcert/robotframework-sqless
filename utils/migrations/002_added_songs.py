old_state = {'Post': {'fields': [{'title': {'field_attrs': {'max_length': 100},
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

actions = {'creations': {'Song': {'fields': [{'title': {'field_attrs': {'max_length': 100},
                                              'field_type': 'CharField'}},
                                   {'artist': {'field_attrs': {'max_length': 100},
                                               'field_type': 'CharField'}},
                                   {'album': {'field_attrs': {'max_length': 100},
                                              'field_type': 'CharField'}},
                                   {'in_collection': {'field_attrs': {'default': False},
                                                      'field_type': 'BooleanField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'song'}}}

new_state = {'Post': {'fields': [{'title': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'content': {'field_attrs': {},
                                  'field_type': 'TextField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'post'},
 'Song': {'fields': [{'title': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'artist': {'field_attrs': {'max_length': 100},
                                 'field_type': 'CharField'}},
                     {'album': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'in_collection': {'field_attrs': {'default': False},
                                        'field_type': 'BooleanField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'song'},
 'User': {'fields': [{'username': {'field_attrs': {'max_length': 20},
                                   'field_type': 'CharField'}},
                     {'email': {'field_attrs': {'max_length': 100},
                                'field_type': 'CharField'}},
                     {'failed_logins': {'field_attrs': {'default': 0},
                                        'field_type': 'IntegerField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}
