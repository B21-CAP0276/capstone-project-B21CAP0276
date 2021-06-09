package com.febrina.vcsapp.data

import android.os.Parcelable
import kotlinx.parcelize.Parcelize



@Parcelize
data class Message(
    var message:String,
    var time:Long
    ):Parcelable