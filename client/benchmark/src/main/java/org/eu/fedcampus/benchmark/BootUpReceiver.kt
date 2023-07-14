package org.eu.fedcampus.benchmark

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.hardware.usb.UsbManager


class BootUpReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        when (intent.action) {
            Intent.ACTION_BOOT_COMPLETED -> launchBenchmarkActivity(context)
        }
    }
}

class UsbReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        when (intent.action) {
            UsbManager.ACTION_USB_ACCESSORY_ATTACHED, UsbManager.ACTION_USB_DEVICE_ATTACHED -> launchBenchmarkActivity(
                context
            )
        }
    }
}

fun launchBenchmarkActivity(context: Context) {
    val launchIntent = Intent(context, BenchmarkActivity::class.java)
    launchIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
    context.startActivity(launchIntent)
}
