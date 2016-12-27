
from lib.util.ops import *
from lib.util.globals import *

def sample(sample_file, sess, config):
    generator = get_tensor("g")[0]
    y_t = get_tensor("y")
    z_t = get_tensor("z")
    dropout_t = get_tensor("dropout")
    categories_t = get_tensor("categories")[0]

    x = np.linspace(0,1, 4)
    y = np.linspace(0,1, 6)

    #z = np.mgrid[-3:3:0.75, -3:3:0.38*3].reshape(2,-1).T
    #z = np.mgrid[-3:3:0.6*3, -3:3:0.38*3].reshape(2,-1).T
    #z = np.mgrid[-6:6:0.6*6, -6:6:0.38*6].reshape(2,-1).T

    z = np.mgrid[-1:1:0.6, -1:1:0.38].reshape(2,-1).T
    #z = np.square(1/z) * np.sign(z)
    #z = np.mgrid[0:1000:300, 0:1000:190].reshape(2,-1).T
    #z = np.mgrid[-0:1:0.3, 0:1:0.19].reshape(2,-1).T
    #z = np.mgrid[0.25:-0.25:-0.15, 0.25:-0.25:-0.095].reshape(2,-1).T
    #z = np.mgrid[-0.125:0.125:0.075, -0.125:0.125:0.095/2].reshape(2,-1).T
    #z = np.zeros(z_t.get_shape())
    #z.fill(0.2)

    categories = np.zeros(categories_t.get_onshape())

    sample = sess.run(generator, feed_dict={z_t: z, dropout_t: 1.0, categories_t: categories})
    print(np.shape(sample))
    #plot(self.config, sample, sample_file)
    stacks = [np.hstack(sample[x*6:x*6+6]) for x in range(4)]
    plot(config, np.vstack(stacks), sample_file)

