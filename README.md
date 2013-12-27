# ansible-deployment

    ---
    - hosts: server
      user: app
      gather_facts: False
      vars:
        user: app
        home_directory: "/home/{{ user }}"
        rails_env: "staging"

      roles:
        -
          role: nicolai86.ansible-deployment

          repo: git@example.com:app
          branch: develop

          deploy_to: "{{ home_directory }}"
          build_path: "{{ deploy_to }}/releases/{{ timestamp.stdout }}"
          shared_path: "{{ deploy_to }}/shared"
          current_path: "{{ deploy_to }}/current"
          migrate: yes
          compile_assets: yes

          symlinks:
            - { src: "{{ shared_path }}/vendor/bundle", dest: "{{ build_path }}/vendor/bundle" }
            - { src: "{{ shared_path }}/public/assets", dest: "{{ build_path }}/public/assets" }
            - { src: "{{ shared_path }}/log", dest: "{{ build_path }}/log" }
            - { src: "{{ shared_path }}/.env", dest: "{{ build_path }}/.env" }
            - { src: "{{ shared_path }}/config/database.yml", dest: "{{ build_path }}/config/database.yml" }

          directories:
            - "{{ shared_path }}/config"

          templates:
            - { src: "templates/env.js", dest: "{{ shared_path }}/.env" }


#### requirements

  - all gem binaries (e.g. bundle, rake, rails) need to be locateable using the $PATH. Make sure to setup properly

#### important features:

  - it can be reused multiple times inside a single playbook for separate deployments.
  - works with rvm, rbenv or system ruby installations.
  - it's using a bare copy of the repository to deploy.
  - migration and asset compilation can be de-activated as needed.
  - only keeps 5 most recent deployments per default

#### limitations

  - does not support rollbacks because ansible does not support error handling (yet)
  - does not contain any restart logic (will change in the future)

#### TODO

  - default values for *_paths
  - default directories