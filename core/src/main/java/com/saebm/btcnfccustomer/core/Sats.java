package com.saebm.btcnfccustomer.core;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * Sats to BTC text for the customer card. The card shows the same number twice: the exact sats the
 * site sent, and the BTC equivalent a reader recognises. Eight decimals always, so a small balance
 * is never rounded away to zero, and the sign of a pending delta is kept.
 */
public final class Sats {
    private Sats() { }

    /** 500 -> "0.00000500"; a negative value keeps its minus sign. */
    public static String btc(long sats) {
        return BigDecimal.valueOf(sats).movePointLeft(8).setScale(8, RoundingMode.UNNECESSARY).toPlainString();
    }

    /** Same value with an explicit plus for a positive delta, matching Response.signed. */
    public static String btcSigned(long sats) {
        return sats >= 0 ? "+" + btc(sats) : btc(sats);
    }
}
