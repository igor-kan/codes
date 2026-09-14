; ModuleID = 'algorithms/02_c/math/mod_inverse.c'
source_filename = "algorithms/02_c/math/mod_inverse.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [49 x i8] c"[C ModInverse] Extended Euclid + Fermat verified\00", align 1
@str.3 = private unnamed_addr constant [52 x i8] c"[C ModInverse] FAILED: non-coprime should return -1\00", align 1
@str.4 = private unnamed_addr constant [40 x i8] c"[C ModInverse] FAILED: inverse mismatch\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(none) uwtable
define dso_local i64 @mod_inv_extended(i64 noundef %0, i64 noundef %1) local_unnamed_addr #0 {
  %3 = alloca i64, align 8
  %4 = alloca i64, align 8
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #6
  %5 = call fastcc i64 @egcd(i64 noundef %0, i64 noundef %1, ptr noundef %3, ptr noundef %4)
  %6 = icmp eq i64 %5, 1
  br i1 %6, label %7, label %13

7:                                                ; preds = %2
  %8 = load i64, ptr %3, align 8, !tbaa !9
  %9 = srem i64 %8, %1
  %10 = icmp slt i64 %9, 0
  %11 = select i1 %10, i64 %1, i64 0
  %12 = add nsw i64 %11, %9
  br label %13

13:                                               ; preds = %2, %7
  %14 = phi i64 [ %12, %7 ], [ -1, %2 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #6
  ret i64 %14
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: write) uwtable
define internal fastcc i64 @egcd(i64 noundef %0, i64 noundef %1, ptr noundef nonnull writeonly captures(none) initializes((0, 8)) %2, ptr noundef nonnull writeonly captures(none) initializes((0, 8)) %3) unnamed_addr #2 {
  %5 = alloca i64, align 8
  %6 = alloca i64, align 8
  %7 = icmp eq i64 %1, 0
  br i1 %7, label %16, label %8

8:                                                ; preds = %4
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %6) #6
  %9 = srem i64 %0, %1
  %10 = call fastcc i64 @egcd(i64 noundef %1, i64 noundef %9, ptr noundef %5, ptr noundef %6)
  %11 = load i64, ptr %6, align 8, !tbaa !9
  %12 = load i64, ptr %5, align 8, !tbaa !9
  %13 = sdiv i64 %0, %1
  %14 = mul nsw i64 %13, %11
  %15 = sub nsw i64 %12, %14
  call void @llvm.lifetime.end.p0(ptr nonnull %6) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #6
  br label %16

16:                                               ; preds = %4, %8
  %17 = phi i64 [ %11, %8 ], [ 1, %4 ]
  %18 = phi i64 [ %15, %8 ], [ 0, %4 ]
  %19 = phi i64 [ %10, %8 ], [ %0, %4 ]
  store i64 %17, ptr %2, align 8, !tbaa !9
  store i64 %18, ptr %3, align 8, !tbaa !9
  ret i64 %19
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(none) uwtable
define dso_local range(i64 -9223372036854775806, 9223372036854775807) i64 @mod_inv_fermat(i64 noundef %0, i64 noundef %1) local_unnamed_addr #3 {
  %3 = icmp sgt i64 %1, 2
  br i1 %3, label %4, label %21

4:                                                ; preds = %2
  %5 = add nsw i64 %1, -2
  br label %6

6:                                                ; preds = %4, %16
  %7 = phi i64 [ %18, %16 ], [ %0, %4 ]
  %8 = phi i64 [ %17, %16 ], [ 1, %4 ]
  %9 = phi i64 [ %19, %16 ], [ %5, %4 ]
  %10 = srem i64 %7, %1
  %11 = and i64 %9, 1
  %12 = icmp eq i64 %11, 0
  br i1 %12, label %16, label %13

13:                                               ; preds = %6
  %14 = mul nsw i64 %10, %8
  %15 = srem i64 %14, %1
  br label %16

16:                                               ; preds = %13, %6
  %17 = phi i64 [ %15, %13 ], [ %8, %6 ]
  %18 = mul nsw i64 %10, %10
  %19 = lshr i64 %9, 1
  %20 = icmp eq i64 %19, 0
  br i1 %20, label %21, label %6, !llvm.loop !11

21:                                               ; preds = %16, %2
  %22 = phi i64 [ 1, %2 ], [ %17, %16 ]
  ret i64 %22
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #4 {
  %1 = alloca i64, align 8
  %2 = alloca i64, align 8
  %3 = alloca i64, align 8
  %4 = alloca i64, align 8
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #6
  %5 = call fastcc i64 @egcd(i64 noundef 3, i64 noundef 1000000007, ptr noundef %3, ptr noundef %4)
  %6 = icmp eq i64 %5, 1
  br i1 %6, label %7, label %13

7:                                                ; preds = %0
  %8 = load i64, ptr %3, align 8, !tbaa !9
  %9 = srem i64 %8, 1000000007
  %10 = icmp slt i64 %9, 0
  %11 = select i1 %10, i64 1000000007, i64 0
  %12 = add nsw i64 %11, %9
  br label %13

13:                                               ; preds = %0, %7
  %14 = phi i64 [ %12, %7 ], [ -1, %0 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #6
  br label %15

15:                                               ; preds = %25, %13
  %16 = phi i64 [ %27, %25 ], [ 3, %13 ]
  %17 = phi i64 [ %26, %25 ], [ 1, %13 ]
  %18 = phi i64 [ %28, %25 ], [ 1000000005, %13 ]
  %19 = urem i64 %16, 1000000007
  %20 = and i64 %18, 1
  %21 = icmp eq i64 %20, 0
  br i1 %21, label %25, label %22

22:                                               ; preds = %15
  %23 = mul nuw nsw i64 %19, %17
  %24 = urem i64 %23, 1000000007
  br label %25

25:                                               ; preds = %22, %15
  %26 = phi i64 [ %24, %22 ], [ %17, %15 ]
  %27 = mul nuw nsw i64 %19, %19
  %28 = lshr i64 %18, 1
  %29 = icmp eq i64 %28, 0
  br i1 %29, label %30, label %15, !llvm.loop !11

30:                                               ; preds = %25
  %31 = icmp eq i64 %14, %26
  br i1 %31, label %32, label %41

32:                                               ; preds = %30
  %33 = mul nuw nsw i64 %14, 3
  %34 = urem i64 %33, 1000000007
  %35 = icmp eq i64 %34, 1
  br i1 %35, label %36, label %41

36:                                               ; preds = %32
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  %37 = call fastcc i64 @egcd(i64 noundef 2, i64 noundef 4, ptr noundef %1, ptr noundef %2)
  %38 = icmp eq i64 %37, 1
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  %39 = select i1 %38, ptr @str.3, ptr @str
  %40 = zext i1 %38 to i32
  br label %41

41:                                               ; preds = %36, %30, %32
  %42 = phi ptr [ %39, %36 ], [ @str.4, %30 ], [ @str.4, %32 ]
  %43 = phi i32 [ %40, %36 ], [ 1, %30 ], [ 1, %32 ]
  %44 = tail call i32 @puts(ptr nonnull dereferenceable(1) %42)
  ret i32 %43
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

attributes #0 = { nofree nosync nounwind sspstrong memory(none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nosync nounwind sspstrong memory(argmem: write) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree norecurse nosync nounwind sspstrong memory(none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"long long", !7, i64 0}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.mustprogress"}
