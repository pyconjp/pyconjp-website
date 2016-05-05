# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #config.vm.box = "chef/centos-6.6"
  config.vm.box = "cent64_x64"
  config.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.4.2/centos64-x86_64-20140116.box"

  config.vm.provider "virtualbox" do |vm|
    # vm.gui = true
    vm.customize [
      'modifyvm', :id,
      '--memory', '2048',
      '--cpus', '1',
      '--name', 'pyconjp-web',
    ]
  end

  config.vm.hostname = "pyconjp-web"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.provision :shell, :inline => "bash /vagrant/scripts/setup-centos.sh"
end
