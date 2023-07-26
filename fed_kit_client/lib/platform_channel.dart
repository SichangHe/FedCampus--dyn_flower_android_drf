import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

class PlatformChannel {
  @visibleForTesting
  final methodChannel = const MethodChannel('fed_kit_flutter');

  Future<String?> getPlatformVersion() async {
    return await methodChannel.invokeMethod<String>('getPlatformVersion');
  }

  Future<int?> connect(int partitionId, Uri host, Uri backendUrl) async {
    return await methodChannel.invokeMethod<int>('connect', {
      'partitionId': partitionId,
      'host': host.toString(),
      'backendUrl': backendUrl.toString()
    });
  }
}
