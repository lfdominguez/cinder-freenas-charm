import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv # noqa 

charms_openstack.charm.use_defaults('charm.default-select-release')

class CinderFreeNASCharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_freenas'
    version_package = 'python-cinder-freenas'
    release = 'ocata'
    packages = [version_package, 'python3-cinder']
    stateless = True
    # Specify any config that the user *must* set.
    mandatory_config = ['nas-login', 'nas-password', 'nas-server-hostname',
                        'nas-iqn-prefix', 'nas-datastore-pool']

    def cinder_configuration(self):
        volume_driver = ('cinder.volume.drivers.ixsystems.iscsi.'
                         'FreeNASISCSIDriver')
        driver_options = [
            ('iscsi_helper', 'tgtadm'),
            ('volume_dd_blocksize', self.config.get('volume-dd-blocksize')),
            ('volume_driver', volume_driver),
            ('ixsystems_login', self.config.get('nas-login')),
            ('ixsystems_password', self.config.get('nas-password')),
            ('ixsystems_server_hostname',
             self.config.get('nas-server-hostname')),
            ('ixsystems_volume_backend_name',
             self.config.get('nas-volume-backend-name')),
            ('ixsystems_iqn_prefix',
             self.config.get('nas-iqn-prefix')),
            ('ixsystems_datastore_pool',
             self.config.get('nas-datastore-pool')),
            ('ixsystems_vendor_name', self.config.get('nas-vendor-name')),
            ('ixsystems_storage_protocol',
             self.config.get('nas-storage-protocol'))]
        return driver_options

class CinderFreeNASCharmRocky(CinderFreeNASCharm):

    # Rocky needs py3 packages.
    release = 'rocky'
    version_package = 'python-cinder-freenas'
    packages = [version_package, 'python3-cinder']
