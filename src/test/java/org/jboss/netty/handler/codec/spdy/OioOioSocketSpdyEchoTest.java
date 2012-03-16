/*
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.jboss.netty.handler.codec.spdy;

import java.util.concurrent.Executor;

import org.jboss.netty.channel.ChannelFactory;
import org.jboss.netty.channel.socket.oio.OioClientSocketChannelFactory;
import org.jboss.netty.channel.socket.oio.OioServerSocketChannelFactory;

public class OioOioSocketSpdyEchoTest extends AbstractSocketSpdyEchoTest {

    @Override
    protected ChannelFactory newClientSocketChannelFactory(Executor executor) {
        return new OioClientSocketChannelFactory(executor);
    }

    @Override
    protected ChannelFactory newServerSocketChannelFactory(Executor executor) {
        return new OioServerSocketChannelFactory(executor, executor);
    }

}
