# ansible-rails-deployment

example usage:

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
          role: nicolai86.ansible-rails-deployment

          repo: git@example.com:app
          branch: develop

          deploy_to: "{{ home_directory }}"
          migrate: yes
          compile_assets: yes
          force_migrate: no
          force_asset_compilation: no

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

          tags: deploy

        -
          role: restart

          service: application:*

          tags:
            - deploy
            - rollback


#### requirements

  - all gem binaries (e.g. bundle, rake, rails) need to be locateable using the $PATH. Make sure to setup properly

#### important features:

  - it can be reused multiple times inside a single playbook for separate deployments.
  - works with rvm, rbenv or system ruby installations.
  - it's using a bare copy of the repository to deploy.
  - migration and asset compilation can be de-activated as needed.
  - only keeps 5 most recent deployments per default

#### limitations

  - you need to write your own restart handling
